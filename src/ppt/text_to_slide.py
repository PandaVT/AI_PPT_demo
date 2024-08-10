# src/ppt/text_to_slide.py
class TextToSlide:
    def __init__(self, max_text_length):
        self.max_text_length = max_text_length

    def split_text(self, text):
        slides = []
        while len(text) > self.max_text_length:
            cut_off = text.rfind(' ', 0, self.max_text_length)
            if cut_off == -1:
                cut_off = self.max_text_length
            slides.append(text[:cut_off])
            text = text[cut_off:].strip()
        slides.append(text)
        return slides

# Example usage
if __name__ == "__main__":
    text_to_slide = TextToSlide(max_text_length=10)
    slides = text_to_slide.split_text("香港特首李家超在首场青年发展高峰论坛上强调年轻人是香港的宝贵资产，并呼吁他们抓住国家发展的机遇。他提到香港政府重视青年发展，致力于培养具有国际视野的新一代，并介绍了香港多元化的教育制度政务司司长陈国基也强调青年发展是香港未来的优先事项，并提到港府将加强爱国教育，增加房屋供应，并推出青年宿舍计划，以支持青年参与社区贡献。")
    print(slides)
