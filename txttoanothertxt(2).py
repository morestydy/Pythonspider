file_path = r"C:\Users\guest0417\Desktop\DCE_MRI_XDJ_Copy.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()
data = data.replace(' ', '').replace('=', '').replace("-", "").replace('\n|', '\n').replace("\n\n", "\n").replace('|', ',')
output_path = file_path.replace('.txt', '.csv')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(data)