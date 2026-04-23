#include <stdio.h>

int main() {
    FILE *arquivo;
    char nome[50], turma[10];
    int idade;

    arquivo = fopen("alunos.txt", "w");

    if (arquivo == NULL) {
        printf("Erro ao criar o arquivo.\n");
        return 1;
    }

    fprintf(arquivo, "Nome/Idade/Turma\n");

    for (int i = 0; i < 10; i++) {
        printf("\nAluno %d\n", i + 1);

        printf("Nome: ");
        scanf(" %[^\n]", nome);  // lê nome com espaço

        printf("Idade: ");
        scanf("%d", &idade);

        printf("Turma: ");
        scanf("%s", turma);

        fprintf(arquivo, "%s/%d/%s\n", nome, idade, turma);
    }

    fclose(arquivo);

    printf("\nArquivo criado com sucesso!\n");

    return 0;
}
