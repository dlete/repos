# Notes

## How to

[Adding default parameter value with type hint in Python](https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python)

<https://www.python.org/dev/peps/pep-3107/#syntax>

[How to Update All of Your Python Packages With pip Using One Simple Command](https://dougie.io/answers/pip-update-all-packages/)

## Math in Markdown and Jupyter notebooks

<https://www.math.ubc.ca/~pwalls/math-python/jupyter/latex>

<https://en.wikibooks.org/wiki/LaTeX/Mathematics>

<https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html>

<https://medium.com/analytics-vidhya/writing-math-equations-in-jupyter-notebook-a-naive-introduction-a5ce87b9a214>

## docker

<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run>
<https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/>
<https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file>
<https://github.com/dockerfile/ubuntu/blob/master/Dockerfile>

```bash
docker build -t myubuntu .
docker run -ti --rm -v ${PWD}:/app myimage
docker run -ti --rm -v ${PWD}:/app 
docker run -ti -v ${PWD}:/app --rm --name test-container myubuntu
```
