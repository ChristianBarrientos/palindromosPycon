from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config

SENDGRID_API_KEY = config('SENDGRID_API_KEY')

def sendMail(resultadosFinales):
    mailSendgrid = Mail(
        from_email='sysadmin@capresca.gob.ar',
        to_emails='christianbarrientos96@gmail.com',
        subject='Resultados Script',
        html_content=resultadosFinales,
        )
    try:
        #print(os.getenv('SENDGRID_API_KEY'))
        #print()
        #sg = SendGridAPIClient(os.getenv(os.environ.get('SENDGRID_API_KEY', '//home/christian/Capresca/palindromosPycon/'))) 
        sg = SendGridAPIClient(SENDGRID_API_KEY) 
        response = sg.send(mailSendgrid)
        if int(response.status_code) != 200 and int(response.status_code) != 202:
            return False, 'No se pudo enviar el correo.'
    except Exception as e:
        print(e)
        return False,e
    return True, 'Enviado'

def esPalindromo(texto):
    #print(texto)
    igual, aux = 0, 0
    for ind in reversed(range(0, len(texto))):
        if texto[ind] == texto[aux]:
            igual += 1
        aux += 1
    if len(texto) == igual:
        #print("El texto es palindromo!")
        #print(texto)
        return texto
    else:
        #print("El texto no es palindromo!")
        return False

def encontrarPalindromos(texto,nombreArchivo):
    bestPalidromo = ''
    bestIndexBase = 0
    bestIndex = 0
    cont = 0
    indexBase = 0
    index = 0
    acu = texto[indexBase]
    texto = texto[::1]
    while (cont != len(texto)):
        try:
            if int(index+1) == len(texto):
                cont = 0
                indexBase = indexBase +1
                index = indexBase
                acu = texto[indexBase]
            else:
                res = esPalindromo(f'{acu}{texto[index+1]}') 
                if res:
                    if len(bestPalidromo) < len(res):
                        bestPalidromo = res
                        bestIndexBase = indexBase
                        bestIndex = index+2

                acu = f'{acu}{texto[index+1]}'
                index +=1
                cont +=1
        except:
            print("Termino: "  +str(nombreArchivo))
            return bestPalidromo,bestIndexBase,bestIndex
    # print(f'{acu}{texto[index+1]}') 
        
def diffArray(array1,array2):
    agrega = len(arrayLeft)+len(arrayRigth)
    if len(array1) >= len(array2):
        for letra in array1:
            if letra in array2:
                agrega -=2
    return agrega


base ='archivos/PALIN'
tipo = '.IN'
resultadosFinales = ''
for num in range(1,11):
    nombreArchivo = f'{base}{num}{tipo}'
    resultadosFinales += str(nombreArchivo)
    fic = open(nombreArchivo, "r")
    lines = fic.readlines()
    #print(lines[0])
    if True: #num == 7:
        #print(lines[1])
        texto = str(lines[1]).strip() #'FFT'  #lines[1] #'FFT' 
        palindromo,indexInferior,indexSuperior = encontrarPalindromos(texto,nombreArchivo)
        arrayLeft = []
        arrayRigth = []
        for i,letra in enumerate(texto[::]):
            if i < indexInferior and i < indexSuperior:
                arrayLeft.append(letra)
            elif i > indexInferior and i >= indexSuperior:
                arrayRigth.append(letra)
        agregaFinal = diffArray(arrayLeft,arrayRigth)
        resultadosFinales += '  Se agregan: 'f'{agregaFinal} '
        resultadosFinales += '  ----  '
        print('Se agregan: 'f'{agregaFinal}')
print(resultadosFinales)
print("Crear archivo Resultados")
archi1=open("resultados.txt","w") 
archi1.write(resultadosFinales+'\n') 
archi1.close() 
print("Envia Mail")
sendMail(resultadosFinales)

"""
print(palindromo)
print(indexInferior)
print(indexSuperior)
print(texto[indexInferior:indexSuperior]) #indexBase:index
"""
#p1AaA1p C9 -- p1AaA1p

#encontrarPali(textoReducidoData,texto)

#esPalindromo(lines[1])
#armarPalindromo(lines[1])

#1AsAp