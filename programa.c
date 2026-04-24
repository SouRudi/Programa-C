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

    printf("Nome: ");

    scanf(" %[^\n]", nome);

    printf("Idade: ");

    scanf("%d", &idade);

    printf("Turma: ");

    scanf("%s", turma);

    fprintf(arquivo, "%s/%d/%s\n", nome, idade, turma);

    fclose(arquivo);

    arquivo = fopen("alunos.txt", "r");

    if (arquivo == NULL) {

        printf("Erro ao abrir para leitura.\n");

        return 1;

    }

    char linha[100];

    printf("\n--- Dados salvos ---\n");

    while (fgets(linha, sizeof(linha), arquivo) != NULL) {

        printf("%s", linha);

    }

    fclose(arquivo);

    return 0;

}
