def guru():
    url = "https://www.guru99.com/automation-testing-interview-questions.html"
    from requests_html import HTMLSession
    print(url)
    session = HTMLSession()
    response = session.get(url)
    raw_reponse = response.html.find('#g-mainbar > div:nth-child(1) > div > div > div > div > div > div:nth-child(3)', first = True).text
    x = [x for x in raw_reponse.split('\n') if "else" not in x]
    data = {}
    for i, v in enumerate(x):
        if v[0].isnumeric():
            data[v] = []
            while i+1<len(x) and not x[i+1][0].isnumeric():
                data[v].append(x[i+1])
                i+=1
            data[v] = "\n".join(data[v])
    print(data)
    import pandas as pd
    col = list(data.keys())
    ind = list(data.values())
    d = {'question' :[], 'ans' : [], 'website':url}
    for i, v in enumerate(col):
        d['question'].append(v)
        d['ans'].append(ind[i])
    df = pd.DataFrame(data= d)
    df.to_csv("t1est.csv")

def win():
    sel = '#loadmore'
    url = "https://www.wisdomjobs.com/e-university/automation-testing-interview-questions.html"
    from requests_html import HTMLSession
    print(url)
    session = HTMLSession()
    response = session.get(url)
    raw_reponse = response.html.find('.interview_questions', first = True).text
    data = {}
    x = [x for x in raw_reponse.split('\n') if "else" not in x]
    print(x)
    for i, v in enumerate(x):
        if v.startswith("Question"):
            data[v] = []
            while i+1 < len(x) and not x[i+1].startswith("Question"):
                data[v].append(x[i+1])
                i+=1
            data[v] = "\n".join(data[v])
    import pandas as pd
    col = list(data.keys())
    ind = list(data.values())
    d = {'question' :[], 'ans' : [], 'website':url}
    for i, v in enumerate(col):
        d['question'].append(v)
        d['ans'].append(ind[i])
    df = pd.DataFrame(data= d)
    df.to_csv("t2est.csv")

def win2():
    url = 'https://www.wisdomjobs.com/e-university/python-automation-testing-interview-questions.html'
    from requests_html import HTMLSession
    print(url)
    session = HTMLSession()
    response = session.get(url)
    raw_reponse = response.html.find('.interview_questions', first = True).text
    data = {}
    x = [x for x in raw_reponse.split('\n') if "else" not in x]
    print(x)
    for i, v in enumerate(x):
        if v.startswith("Question"):
            data[v] = []
            while i+1 < len(x) and not x[i+1].startswith("Question"):
                data[v].append(x[i+1])
                i+=1
            data[v] = "\n".join(data[v])
    import pandas as pd
    col = list(data.keys())
    ind = list(data.values())
    d = {'question' :[], 'ans' : [], 'website':url}
    for i, v in enumerate(col):
        d['question'].append(v)
        d['ans'].append(ind[i])
    df = pd.DataFrame(data= d)
    df.to_csv("t3est.csv")
def guru2():
    url = "https://www.guru99.com/top-100-selenium-interview-questions-answers.html"
    from requests_html import HTMLSession
    print(url)
    session = HTMLSession()
    response = session.get(url)
    raw_reponse = response.html.find('#g-mainbar > div:nth-child(1) > div > div > div > div > div > div:nth-child(3)', first = True).text
    x = [x for x in raw_reponse.split('\n') if "else" not in x]
    data = {}
    for i, v in enumerate(x):
        if v[0].isnumeric():
            data[v] = []
            while i+1<len(x) and not x[i+1][0].isnumeric():
                data[v].append(x[i+1])
                i+=1
            data[v] = "\n".join(data[v])
    print(data)
    import pandas as pd
    col = list(data.keys())
    ind = list(data.values())
    d = {'question' :[], 'ans' : [], 'website':url}
    for i, v in enumerate(col):
        d['question'].append(v)
        d['ans'].append(ind[i])
    df = pd.DataFrame(data= d)
    df.to_csv("t4est.csv")
