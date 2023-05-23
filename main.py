import lxml.etree as ET
import pandas as pd

# 解析XML文件
tree = ET.parse('3.xml', parser=ET.XMLParser(encoding='GB18030', recover=True))
root = tree.getroot()

# 创建空的DataFrame
df = pd.DataFrame()

# 递归函数，用于遍历XML元素并提取数据
def parse_element(element, row):
    for child in element:
        if len(child) == 0:
            row[child.tag] = child.text
        else:
            parse_element(child, row)

# 提取XML数据并填充到DataFrame中
for element in root.findall('.//Row'):
    row = {}
    for key, value in element.attrib.items():
        row[key] = value
    parse_element(element, row)
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

# 将数据写入Excel文件
df.to_excel('output.xlsx', index=False)
