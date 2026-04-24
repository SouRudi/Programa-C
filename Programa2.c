#include <stdio.h>

int main() {

    FILE *f;

    int id, op = 1;

    char nome[50], turma[10];

    while (op != 0) {



        f = fopen("alunos.txt", "r");

        printf("\n--- ALUNOS ---\n");

        if (f != NULL) {

            while (fscanf(f, "%d %s %s", &id, nome, turma) == 3) {

                printf("ID: %d | Nome: %s | Turma: %s\n", id, nome, turma);

            }

            fclose(f);

        }



        printf("\nDigite 1 para cadastrar ou 0 para sair: ");

        scanf("%d", &op);

        if (op == 1) {

            printf("ID: ");

            scanf("%d", &id);

            printf("Nome: ");

            scanf("%s", nome);

            printf("Turma: ");

            scanf("%s", turma);

            f = fopen("alunos.txt", "a");

            fprintf(f, "%d %s %s\n", id, nome, turma);

            fclose(f);

        }

    }

    return 0;

}
