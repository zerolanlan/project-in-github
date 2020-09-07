from aip import AipOcr

APP_ID = '11275821'

API_KEY = 'Ozk7kam7ZdO3BmmqeusCr2Rc'

SECRET_KEY = 'tNq2yIwEG29CK8FXLGkXoclrDrhBQS3E'



client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):

    with open(filePath, 'rb') as fp:

        return fp.read()



image = get_file_content('example.jpg')

def get_file_content(filePath):

    with open(filePath, 'rb') as fp:

        return fp.read()



image = get_file_content('example.jpg')

idCardSide = "back"

listResult=[]

result=client.idcard(image, idCardSide);

print(result)

data=result['data']

word_result=data['words_result']

listResult.append(world_result['姓名']['word'])

listResult.append(world_result['性别']['word'])

listResult.append(world_result['民族']['word'])

listResult.append(world_result['出生']['word'])

listResult.append(world_result['住址']['word'])

listResult.append(world_result['公民身份证号码']['word'])

for li in listResult:

    print(li)
