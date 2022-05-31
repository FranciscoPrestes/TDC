import git
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def PullGit(caminho_repo,caminho_clone):

    try:
        git.Repo.clone_from(caminho_repo, caminho_clone)
        resposta='Repositório clonado para a máquina'
    except:
        g=git.cmd.Git(caminho_clone)
        g.pull()
    return caminho_clone
    
def PushGit(caminho_repo,caminho_clone):
    try:
        repo = git.Repo(caminho_clone)
        files = repo.git.diff(None, name_only=True)
        print(files)
        for f in files.split('\n'):
            caminho=caminho_clone + '\\' + f
            repo.git.add(caminho)
        repo.git.commit('-m','TDC', author='fernanda.paulino1@gmail.com')
        repo.git.push()
        return 'Repositório atualizado. Em que mais posso ajudar?'
    except:
        return 'Repositório atualizado. Em que mais posso ajudar?'
    
    
def ApplyScript(caminho_script,nome_script, nome_banco):

	# Abrimos uma conexão com o banco de dados:
    conexao = pymysql.connect(db='INFORMATION_SCHEMA', user='root', passwd='fer061025')
    cursor = conexao.cursor()
    cursor.execute("Select schema_name from schemata where schema_name='" + nome_banco + "'")
    linha=cursor.fetchone()
    cursor.close
    arquivo=caminho_script + "\\" + nome_script
    if linha==None:
        with open(arquivo,'r') as abre_sql: 
            arq_sql=abre_sql.read()
            arq_quebrado=arq_sql.split('GO')
            for parte in arq_quebrado:
                if parte!='':
                    cursor.execute(parte)
    else:
        conexao.close
        conexao = pymysql.connect(db=nome_banco, user='root', passwd='fer061025')
        with open(arquivo,'r') as abre_sql: 
            arq_sql=abre_sql.read()
            arq_quebrado=arq_sql.split('GO')
            for parte in arq_quebrado:
                if parte!='':
                    cursor.execute(parte)

def OpenPage():

    nav=webdriver.Chrome();
    nav.maximize_window()
    nav.get('https://web.pontoicarus.com.br/app');
    nav.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/form/div[2]/div/input').send_keys('fernanda.paulino1@gmail.com')
    nav.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/form/div[4]/div/input').send_keys('Fer@060878')
    nav.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/form/div[4]/div/input').send_keys(Keys.ENTER)
    time.sleep(3)
    return('Prontinho já pode bater o ponto, tamo junto')