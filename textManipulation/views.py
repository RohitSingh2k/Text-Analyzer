from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    initial_text = request.POST.get('text','default')

    decapitalize = request.POST.get('decapitalize','off')
    rmpunc = request.POST.get('rmpunc','off')
    rmspace = request.POST.get('rmspace','off')
    rmnewline = request.POST.get('rmnewline','off')

    analyzed = ''
    operation_performed = 'Text after'
    if decapitalize != 'off':
        for i in initial_text:
            analyzed = analyzed + i.lower()
        initial_text = analyzed
        analyzed = ''
        operation_performed = operation_performed + ' decapitalizing charcters,'

    if rmpunc != 'off':
        punc = '''?/.>,<\\';][}{|":()*&^%$#@!~`'''
        for i in initial_text:
            if i not in punc:
                analyzed = analyzed + i.lower()
        initial_text = analyzed
        analyzed = ''
        operation_performed = operation_performed + ' removing punctuations,'
    
    if rmspace != 'off':
        for i in range(len(initial_text)):
            if initial_text[i] == ' ' and initial_text[i+1] == ' ':
                pass
            else:
                analyzed = analyzed + initial_text[i]
        initial_text = analyzed
        analyzed = ''
        operation_performed = operation_performed +  ' removing extraspaces,'
    
    if rmnewline != 'off':
        for i in initial_text:
            if i == '\n' or i == '\r':
                pass
            else:
                analyzed = analyzed + i
            
        initial_text = analyzed
        analyzed = ''
        operation_performed = operation_performed + ' removing newline,'
    
    else:
        operation_performed = operation_performed + ' doing no operation on it,'
    
    # operation_performed = operation_performed[:len(operation_performed-2)]
    operation_performed = operation_performed.strip(',')
    operation_performed = operation_performed + '.'

    params = {'text':initial_text, 'operations': operation_performed }
    return render(request, 'analyze.html',params)