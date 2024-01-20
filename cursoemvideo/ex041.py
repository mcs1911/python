from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f' Você tem \033[36m{idade} anos\033[m e se classifica na categoria \033[1;35;46mMIRIM')
elif 9 <= idade < 14:
    print(f' Você tem \033[33m{idade} anos\033[m e se classifica na categoria \033[1;35;43mINFANTIL\033[m') 
elif 14 <= idade < 19:
    print(f' Você tem \033[35m{idade} anos\033[m e se classifica na categoria \033[1;35;47mJUNIOR')
elif 19 <= idade <= 20:
    print(f' Você tem \033[32m{idade} anos\033[m e se classifica na categoria \033[1;35;42mSÊNIOR')
else:
    print(f' Você tem \033[31m{idade} anos\033[m e se classifica na categoria \033[1;37;41mMASTER')
