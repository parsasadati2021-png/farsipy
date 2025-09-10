from .farsi_map import فارسی_به_انگلیسی
import re

class FarsiPython:
    def __init__(self):
        self.map = فارسی_به_انگلیسی
        self.number_map = {
            '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
            '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
        }
    
    def translate_numbers(self, text):
        for fa_num, en_num in self.number_map.items():
            text = text.replace(fa_num, en_num)
        return text
    
    def translate(self, farsi_code):
        translated_code = farsi_code
        # اول اعداد رو تبدیل کن
        translated_code = self.translate_numbers(translated_code)
        
        # تبدیل کلمات کلیدی (فقط خارج از strings و comments)
        lines = translated_code.split('\n')
        for i, line in enumerate(lines):
            in_string = False
            new_line = []
            j = 0
            while j < len(line):
                if line[j] in ('"', "'"):
                    in_string = not in_string
                    new_line.append(line[j])
                    j += 1
                elif not in_string and line[j:j+1] == '#':
                    # بقیه خط comment هست
                    new_line.append(line[j:])
                    break
                elif not in_string:
                    # خارج از string هستیم
                    for fa, en in self.map.items():
                        if line.startswith(fa, j) and (j + len(fa) == len(line) or not line[j + len(fa)].isalpha()):
                            new_line.append(en)
                            j += len(fa)
                            break
                    else:
                        new_line.append(line[j])
                        j += 1
                else:
                    # داخل string هستیم
                    new_line.append(line[j])
                    j += 1
            lines[i] = ''.join(new_line)
        
        return '\n'.join(lines)
    
    def run(self, farsi_code):
        english_code = self.translate(farsi_code)
        exec(english_code)
    
    def run_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            farsi_code = f.read()
        self.run(farsi_code)

# برای استفاده آسان
fp = FarsiPython()
