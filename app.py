import gradio as gr

from point_load_to_ucs_converter import (
    CUSTOM_LABEL,
    DEFAULT_ROCK_TYPE,
    ROCK_TYPE_OPTIONS,
    compute_point_load_to_ucs,
)

INFO_HTML = """
<details style="margin-top: 2.25em; font-size: 14px;">
  <summary>ℹ️ ISRM UCS classification</summary>
  <table style="margin-top: 8px; border-collapse: collapse;">
    <tr><th style="text-align:left;padding:4px 8px;">UCS (MPa)</th><th style="text-align:left;padding:4px 8px;">Classification</th></tr>
    <tr><td style="padding:4px 8px;">&lt; 1</td><td style="padding:4px 8px;">Extremely weak</td></tr>
    <tr><td style="padding:4px 8px;">1 – 5</td><td style="padding:4px 8px;">Very weak</td></tr>
    <tr><td style="padding:4px 8px;">5 – 25</td><td style="padding:4px 8px;">Weak</td></tr>
    <tr><td style="padding:4px 8px;">25 – 50</td><td style="padding:4px 8px;">Medium strong</td></tr>
    <tr><td style="padding:4px 8px;">50 – 100</td><td style="padding:4px 8px;">Strong</td></tr>
    <tr><td style="padding:4px 8px;">100 – 250</td><td style="padding:4px 8px;">Very strong</td></tr>
    <tr><td style="padding:4px 8px;">&gt; 250</td><td style="padding:4px 8px;">Extremely strong</td></tr>
  </table>
</details>
"""


def toggle_custom_k(rock_type):
    return gr.update(visible=rock_type == CUSTOM_LABEL)


def convert(is50, rock_type, custom_k):
    _, message = compute_point_load_to_ucs(is50, rock_type, custom_k)
    return message


with gr.Blocks(title="Point Load to UCS Converter") as demo:
    gr.Markdown("# Point Load to UCS Converter")
    gr.Markdown("Convert point load strength index (Is50) to uniaxial compressive strength (UCS) using UCS = k × Is50.")

    with gr.Row():
        is50_input = gr.Number(
            label="Point Load Index Is50 [MPa]",
            value=1.0,
            precision=4,
        )
        rock_type_input = gr.Dropdown(
            label="Rock type",
            choices=ROCK_TYPE_OPTIONS,
            value=DEFAULT_ROCK_TYPE,
        )

    custom_k_input = gr.Number(
        label="Custom k factor (15–30)",
        value=24.0,
        precision=2,
        visible=False,
    )

    convert_button = gr.Button("Convert", variant="primary")

    with gr.Row():
        result_output = gr.Textbox(
            label="Result",
            value="UCS = 24.00 MPa – Classification: Strong",
            interactive=False,
            scale=5,
        )
        info_output = gr.HTML(INFO_HTML)

    rock_type_input.change(
        fn=toggle_custom_k,
        inputs=rock_type_input,
        outputs=custom_k_input,
    )

    convert_button.click(
        fn=convert,
        inputs=[is50_input, rock_type_input, custom_k_input],
        outputs=result_output,
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
