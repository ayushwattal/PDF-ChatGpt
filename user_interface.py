import gradio as gr

# Gradio application setup
def create_demo():
    with gr.Blocks(title= " PDF Chatbot",
        theme = "Soft"  # Change the theme here
        ) as demo:
        
        # Create a Gradio block

        with gr.Column():
            with gr.Row():
                with gr.Column(scale=0.8):
                    api_key = gr.Textbox(
                        placeholder='Enter your OpenAI API key',
                        show_label=False,
                        interactive=True,
                    container=False)
                    
                with gr.Column(scale=0.2):
                    change_api_key = gr.Button('Update API Key')

            with gr.Row():
                chatbot = gr.Chatbot(value=[], elem_id='chatbot', height=680)
                show_img = gr.Image(label='PDF Preview', tool='select', height=680)

        with gr.Row():
            with gr.Column(scale=0.60):
                text_input = gr.Textbox(
                    show_label=False,
                    placeholder="Ask your pdf?",
                container=False)

            with gr.Column(scale=0.20):
                submit_btn = gr.Button('Send')

            with gr.Column(scale=0.20):
                upload_btn = gr.UploadButton("📁 Upload PDF", file_types=[".pdf"])
                

        return demo, api_key, change_api_key, chatbot, show_img, text_input, submit_btn, upload_btn

if __name__ == '__main__':
    demo, api_key, change_api_key, chatbot, show_img, text_input, submit_btn, upload_btn = create_demo()
    demo.queue()
    demo.launch()

