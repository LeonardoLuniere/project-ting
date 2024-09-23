from ting_file_management.queue import Queue


def exists_word(word, instance):
    word = word.lower()
    search_result = []

    for file in instance._data:
        lines = file["linhas_do_arquivo"]
        occurrences = []

        for index, line in enumerate(lines):
            line = line.lower()
            if word in line:
                occurrences.append({"linha": index + 1})

        if len(occurrences):
            search_result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return search_result


def search_by_word(word, instance):
    word = word.lower()
    search_result = []

    for file in instance._data:
        lines = file["linhas_do_arquivo"]
        occurrences = []

        for index, line in enumerate(lines):
            line_to_lower = line.lower()
            if word in line_to_lower:
                occurrences.append({
                    "linha": index + 1,
                    "conteudo": line
                })

        if len(occurrences):
            search_result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return search_result


text_file = [
        "Acima de tudo,",
        "é fundamental ressaltar que a adoção de "
        "políticas descentralizadoras nos obriga",
        "à análise do levantamento das variáveis envolvidas.",
]

text1 = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": text_file,
}

queue = Queue()
queue.enqueue(text1)

print(exists_word('de', queue))
