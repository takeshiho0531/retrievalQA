import gradio as gr

from retrieval import retrieve

with gr.Blocks() as demo:
    gr.Markdown(
        """
    # Retrieval for 情報通信システム創成学
    <br>
    <br>

    query と書かれた左のboxに本講義の内容に関する質問を入力して送信のボタンを押すと、右側のboxに講義資料中のどこを参照するとよさそうかというのが表示されます。
    <br>
    <br>
    合計5つのpdfが表示されると思われますが、左に表示されているものの方が参考になる確率が高いと思われます。
    <br>
    <br>

    pdfの表示としては、"chap??"の部分が何章かを、その後の数字は何枚目かを示しています。講義資料は全て配布されたものをもとにしていて、日本語訳された資料は使用していません。
    <br>
    <br>

    なお、queryに入力するのは英語のほうがよさそうです。
    <br>
    <br>
    <br>
    <br>

    """
    )

    gr.Interface(fn=retrieve, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(share=True)
