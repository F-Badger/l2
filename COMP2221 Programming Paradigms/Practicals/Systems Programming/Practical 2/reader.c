#include <string.h>
#include "reader.h"

int contains_token(const char *line, const char *token) {
return (strstr(line, token) != NULL);
}
