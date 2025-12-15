Reference:
https://www.youtube.com/watch?v=6xYaFNhvgx8&list=PLhr0Ua8H1x-K7UMXXeSfjULEIBCE1FVd1&index=3

Commiting to github via PS Terminal:
1- First the code files (and req.txt) should all be under the project folder _not_ the venv folder. Moved them manually.
2- On the terminal:
> git add text-classification/*
> git commit -m "Initial commit for text classfxn project"
 2 files changed, 21 insertions(+)
 create mode 100644 text-classification/requirements.txt
 create mode 100644 text-classification/sentiment-analyzer.py
> git push --set-upstream origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 727 bytes | 121.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/the-menna-sherif/GenAIProjects.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
> git status
(venv) PS C:\Users\msherif\PycharmProjects\GenAIProjects> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

primitive Gradio GUI:
<img width="952" height="268" alt="image" src="https://github.com/user-attachments/assets/83602c19-13df-429a-b8d4-605c2a08b9cc" />

Dynamic Gradio GUI- this is after modifying the code to accept .xlsx type files and return a pandas df with the review & sentiment:
<img width="1900" height="729" alt="image" src="https://github.com/user-attachments/assets/9952866e-f900-47be-a0d0-b264d493886e" />


