#include <stdio.h>

int shortestString(char s[]) {
    int start = 0, end = 0, min_length = 100000; 
    int has_a = 0, has_z = 0; 

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'a') has_a = 1;
        if (s[i] == 'z') has_z = 1;
    }

    if (!has_a || !has_z) return -1; 
    while (s[end] != '\0') {
        if (s[end] == 'z') {
            while (s[start] != 'a') {
                start++;
            }
            int current_length = end - start + 1;
            if (current_length < min_length) {
                min_length = current_length;
            }
        }
        end++;
    }

    return min_length;
}

int main() {
    char s[100000]; // Đặt giới hạn độ dài xâu
    printf("Nhap xau S: ");
    scanf("%s", s);

    int result = shortestString(s);
    if (result == -1) {
        printf("Khong ton tai xau thoa man yeu cau.\n");
    } else {
        printf("Do dai xau ngan nhat thoa man yeu cau: %d\n", result);
    }

    return 0;
}
