# Git Credential Manager
# Use \n for new line \t for tab

# .ssh/config file content
text_content = ["#Account1\nHost github.com\n\tHostName github.com\n\tUser git\n\tIdentityFile ~/.ssh/account1","#Account2\nHost github.com\n\tHostName github.com\n\tUser git\n\tIdentityFile ~/.ssh/account2","#Account3\nHost github.com\n\tHostName github.com\n\tUser git\n\tIdentityFile ~/.ssh/account3"]
# .gitconfig file content
global_content = ["[user]\n\tsigningkey = keyid_for_account1\n\tname = username_account1\n\temail = email.account.1@gmail.com\n[commit]\n\tgpgsign = true\n","[user]\n\tsigningkey = keyid_for_account2\n\tname = username_account2\n\temail = email.account.2@gmail.com\n[commit]\n\tgpgsign = true\n", "[user]\n\tsigningkey = keyid_for_account3\n\tname = username_account3\n\temail = email.account.3@gmail.com\n[commit]\n\tgpgsign = true\n",]
# text for user interface feedback
options = ["Account1", "Account2", "Account3"]
# git ssh key file path
config_file_path = "/Users/macosuser/.ssh/config"
#.gitconfig filepath
global_config_file_path = "/Users/macosuser/.gitconfig"


def select_value (config_options):
    print ("select account")
    print ("--------------")
    print ("")
    print ("0) Account1")
    print ("1) Account2)
    print ("2) Account3")
    print ("")
    selected_value = input ("Enter your value: ")
    print ("\nSelected Account: " + config_options[int(selected_value)])
    output_int = int(selected_value)
    return output_int

def write_text (file_path, file_text):
    with open(file_path, 'w') as f:
        f.write(file_text)

selected_profile = select_value(options)
write_text (config_file_path, text_content[selected_profile])
write_text (global_config_file_path, global_content[selected_profile])
print ("\n**********")
print ("*  Done  *")
print ("**********")
print ("")