from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#'preciso clonar um repositório','pullgit','ok , clone saindo',

sentence_list=['preciso marcar minhas férias','entre no painel principal de pessoas, na página principal da companhia, e escolha a opção minhas férias. Em que mais posso ajudar? ','0',
'preciso pegar meu informe de rendimentos','entre no painel principal de pessoas, na página principal da companhia, e escolha a opção documentos e depois informe de rendimentos. Em que mais posso ajudar?','0',
'preciso atualizar o repositório','ok , atualizando','1',
'preciso subir um banco de dados','qual o nome do banco de dados?','2',
'só isso obrigada','por nada, tamo junto','3']

#1 - pushgit
#2 - applyscript


def bot_response(user_input):
    exp=''
    user_input=user_input.lower()
    quebras=user_input.split(" ")
    for quebra in quebras:
        if quebra.lower() not in ('com','de','para','pra','a', 'o', 'e','do','da','dele','dela','minha','minhas','sua','problema','problemas','máquina','quem','onde','quando','é','foi','por que','porque', 'por isso', 'isso', 'aquilo','disto','daquilo','como','preciso','um','uma','em','do','qual','ok'):
            exp=exp + ' ' + quebra
    sentence_list.append(exp)
    bot_response=''
    cm=CountVectorizer().fit_transform(sentence_list) # cria vetor indicando a quantidade de vezes que cada palavra aparece nafrase.
    similarity_scores=cosine_similarity(cm[-1],cm) #calcula o coseno de similaridade da comparação enter as expressões da lista e a expressão digitada
    similarity_scores_list=similarity_scores.flatten()
    response_flag=0
    j=0
    cont=1
    for i in range(len(similarity_scores_list)-1):
        if similarity_scores_list[i]>0.0:
            response_flag=1
            if cont==1:
                major=similarity_scores_list[i]
                cont=cont+1
                indice=i
            else:
                if similarity_scores_list[i]>major:
                    major=similarity_scores_list[i]
                    indice=i
                cont=cont+1    
                    
    if response_flag==0:
        resp=''
        recebe=''
    else:
        if sentence_list[indice+2]=='0':
            resp=sentence_list[indice +1]
            recebe='0'
        else:
            resp=sentence_list[indice+1]
            recebe=sentence_list[indice+2]

    bot_response=resp
    resposta=[]
    resposta.append(bot_response)
    resposta.append(recebe)
    sentence_list.remove(exp)
    return resposta