def wolfquery(question):
    import wolframalpha
    client = wolframalpha.Client('R33RAT-7QTK4AL8LL')
    res = client.query(question)
    return(next(res.results).text)
