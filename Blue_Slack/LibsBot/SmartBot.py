#bibliotecas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#lista de sentenças (pergunta/resposta)
sentence_list=['blue','Olá, em que posso ajudar?',
'conexão VPN','Qual mensagem de erro aparece?',
'não foi possível acessar','Sua senha está vencida entre em https://atualizar-senha.com.br',
'sysgen não abre','Entre na central de software e reinstale o aplicativo',
'network connection unreachable','Reinicie o modem wifi e a máquina e tente conectar novamente']

#rotina que encontra o maior valor da lista de cossenos de similaridade
def major_value(list): 
    cont=1
    index=-1
    for i in range(len(list)-1):
        if list[i]>0.0:
            response_flag=1
            if cont==1:
                major=list[i]
                cont=cont+1
                index=i
            else:
                if list[i]>major:
                    major=list[i]
                    index=i
                cont=cont+1    
    return index

#limpa a sentença enviada pelo usuário retirando expressões irrelevantes
def clean_sentence(sentence): 
    exp=''
    quebras=sentence.split(" ")
    for quebra in quebras:
        if quebra.lower() not in ('the', 'is','com','de','para','pra','a', 'o', 'e','do','da','dele','dela','minha','sua','problema','problemas','máquina','quem','onde','quando','é','foi','por que','porque', 'por isso', 'isso', 'aquilo','disto','daquilo','como','preciso','um','uma','em','do','qual','ok','estou','problema','problemas','na','no'):
            exp=exp + ' ' + quebra
    return exp

#rotina que utiliza a biblioteca de machine learning
def bot_response(user_input):  
    user_input=user_input.lower() #recebe mensagem enviada pelo usuário
    sentence=clean_sentence(user_input) #faz limpeza na expressão enviada pelo usuário
    sentence_list.append(sentence)#inclui a sentença limpa enviada pelo usuário na lista de sentenças existentes
    cm=CountVectorizer().fit_transform(sentence_list) # cria vetor indicando a quantidade de vezes que cada palavra aparece na frase.
    print(cm[-1])
    similarity_scores=cosine_similarity(cm[-1],cm) #calcula o cosseno de similaridade da comparação enter as expressões da lista criada e a lista contendo a expressão digitada
    similarity_scores_list=similarity_scores.flatten() #coloca os resultados em lista
    print(similarity_scores_list)
    ind=major_value(similarity_scores_list) # encontra o maior valor da lista
    if ind==-1: 
        resposta='Não tenho essa mensagem em minha base' # se não encontrou nenhuma similaridade
    else:
        resposta=sentence_list[ind+1] #se encontrou similaridades

    sentence_list.remove(sentence) #remove a sentença do usuário da lista
    return resposta #retorna a resposta