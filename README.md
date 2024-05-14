# AI_PPT_demo
This repo is built to show how to generate PPT using python

## Installation

To install the necessary dependencies, follow the steps below:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/PandaVT/AI_PPT_demo.git
cd AI_PPT_demo
```

2. Create and activate a Conda environment using the provided YAML file:

```
conda env create -f config/env.yml && conda clean -afy
conda activate AI_PPT
```

3. Install additional dependencies using pip:

```
conda run --no-capture-output --name AI_PPT pip install --no-cache-dir python-pptx==0.6.23 retry -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## How to use

```
python generate_ppt.py 
```
