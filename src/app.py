# src/app.py
import yaml
from ppt.ppt_generator import PPTGenerator
from ppt.text_to_slide import TextToSlide
from model.llm_integration import LLMIntegration
import os

if __name__ == "__main__":
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    sys_prompt = ""
    prompt = "Generate a summary for the following text: "
    content = """
    香港特首李家超称，年轻人是香港重要的资产，呼吁香港年轻人要把握国家发展的机会，未来就在他们手中。综合《星岛日报》和网媒“香港01”报道，香港首场青年发展高峰论坛星期六（8月10日）举行，这场活动由民政与青年事务局主办，来自中国大陆、马来西亚、老挝等地的2000人与会。李家超在会上致辞时说，世界各地人士到香港参与论坛，显示青年发展的重要性。他称，香港是释放年轻人潜力的一个很好地方，港府重视青年发展，希望培养新一代具有国际视野的年轻人。李家超说，香港有多元化全面教育制度，包括五所大学名列全球100名，有很多顶尖学系及职业、专业教育，培育年轻人多元发展，欢迎全世界人士到香港读书。李家超还说，港府在2022年底推出各项人才计划，过去19个月收到超过34万宗申请，目前已审批21万宗申请。他说，在国家政策不断支持下，香港发展潜力无限，鼓励年轻人利用机遇融入发展。针对巴黎奥运赛事即将结束，李家超说，香港人对香港运动员引以为傲，运动员所展示的团队精神等都是香港精神的特质。他强调，港人要更快、更高、更强去追求目标，而香港是实现目标的好地方。香港政务司司长陈国基致辞时则指出，青年发展是未来优先事项，香港繁荣与青年发展息息相关。他表示，希望香港青年了解中国历史及文化，港府会加强宣扬爱国教育。房屋方面，他说，港府会增加房屋供应，推出青年宿舍计划，也会提供多渠道让青年参与社区作出贡献。
    """
    messages = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": prompt + content}]

    # Initialize LLM integration
    llm = LLMIntegration(
        api_key=config['language_model']['api_key'],
        base_url=config['language_model']['base_url'],
        model_name=config['language_model']['model_name'],
        max_tokens=config['language_model']['max_tokens'],
        temperature=config['language_model']['temperature']
    )

    generated_title = llm.generate_text(messages)


    text_to_slide = TextToSlide(max_text_length=50)
    split_texts = text_to_slide.split_text(content)

    slides_content = []

    for i, text in enumerate(split_texts):
        slide = {
            "title": generated_title if i == 0 else f"Continued: {generated_title}",
            "content": text,
            "background": os.path.join(config['data']['backgroud_path'], "bird.jpg") if i % 2 == 0 else None,
            "title_position": {"left": 1, "top": 0.5} if i % 2 == 0 else {"left": 0, "top": 1.5},
            "content_position": {"left": 1, "top": 2.5} if i % 2 == 0 else {"left": 0.1, "top": 3},
            "image": None if i % 2 == 0 else os.path.join(config['data']['backgroud_path'], "demo.jpg")
        }
        slides_content.append(slide)

    # Generate PPT
    ppt_generator = PPTGenerator(config)
    output_file = ppt_generator.create_presentation(slides_content)
    print(f"Presentation saved as {output_file}")
