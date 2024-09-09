with open('encrypted_message_two.txt', 'r') as file:
    encrypted_message = file.read()

message_list = list(encrypted_message)

start = 1
end = len(message_list) - 2

while start < end:
    message_list[start], message_list[end] = message_list[end], message_list[start]
    start += 2
    end -= 2

decrypted_message = ''.join(message_list)

print(decrypted_message)
