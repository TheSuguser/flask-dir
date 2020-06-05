import os 
import sys 
import shutil
import re

class Template(object):
    def __init__(self):
        DIR_PATH = os.path.dirname(__file__)
        self.TEMPLATE_PATH = os.path.abspath(os.path.join(DIR_PATH, 'template'))
        self.CWD = os.getcwd()
    
    def handle(self, args):
        self.name = args.get('<name>')
        if self.name is None:
            raise ValueError('Project name is empty')
        target_dir = os.path.join(self.CWD, self.name)
        if os.path.exists(target_dir):
            raise ValueError('Project exists')
        
        # copy from template
        shutil.copytree(self.TEMPLATE_PATH, target_dir)

        # modify template
        for root, dirs, files in os.walk(target_dir):
            for f in files:
                if f in ['app.py', '__init__.py']:
                    file_path = os.path.join(root, f)
                    with open(file_path, mode='r', encoding="utf-8") as fr:
                        old_content = fr.read()
                    new_content = re.sub('appname', self.name, old_content)                 
                    with open(file_path, mode='w', encoding='utf-8') as fw:
                        fw.write(new_content)
    
    def validate_name(self,name):
        pass
