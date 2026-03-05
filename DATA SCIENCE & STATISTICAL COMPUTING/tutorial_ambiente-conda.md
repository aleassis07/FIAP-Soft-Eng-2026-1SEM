# Utilizando o arquivo environment.yml

Você **não precisa criar um `environment_dpsc.yml` para cada pasta de aula**. O ideal é ter **um único ambiente central para toda a disciplina**. 👍

Pela estrutura que você mostrou:

```
DATA SCIENCE & STATISTICAL COMPUTING
│
├── aula_02_12_2026
│   └── notebook.ipynb
│
├── aula_02_19_2026
│   └── notebook.ipynb
│
├── aula_02_26_2026
│   └── notebook.ipynb
│
├── aula_03_05_2026
│   └── notebook.ipynb
│
└── environment_dpsc.yml
```

Esse **`environment_dpsc.yml` na raiz da pasta** já é suficiente.

---

## Como isso funciona na prática

O `environment.yml` **define um ambiente Conda**, não um ambiente por pasta.

Ou seja:

1️⃣ Você cria o ambiente **uma vez**:

```bash
conda env create -f environment_dpsc.yml
```

ou

```bash
mamba env create -f environment_dpsc.yml
```

2️⃣ Ativa o ambiente:

```bash
conda activate dpsc
```

3️⃣ Abre o Jupyter:

```bash
jupyter lab
```

ou

```bash
jupyter notebook
```

4️⃣ Qualquer notebook dentro dessas pastas:

```
aula_02_12_2026/
aula_02_19_2026/
aula_02_26_2026/
```

vai usar **o mesmo ambiente**.

---

## Por que **não** criar vários environments

Criar um ambiente por aula seria ruim porque:

* ocupa **muito espaço**
* demora para instalar dependências
* fica difícil manter
* quase sempre as aulas usam **as mesmas bibliotecas**

Exemplo típico de libs:

```
python
numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
```

Isso é **comum para todo o curso**.

---

## Regra usada em projetos de Data Science

Normalmente fica assim:

```
projeto/
│
├── data/
├── notebooks/
│   ├── aula_01.ipynb
│   ├── aula_02.ipynb
│   └── aula_03.ipynb
│
├── src/
│
├── environment.yml
└── README.md
```

Ou seja:
👉 **1 environment para o projeto inteiro**

---

💡 **Dica importante para evitar erro depois**

Depois de criar o environment, registre ele no Jupyter:

```bash
python -m ipykernel install --user --name dpsc --display-name "Python (DPSC)"
```

Assim seus notebooks sempre usarão o **kernel correto**.

---

Se quiser, também posso te mostrar **uma estrutura de pastas ideal para projetos de Data Science na faculdade** (que evita muita bagunça quando começam os trabalhos e projetos maiores).


# Ativando o ambiente na faculdade

Quando você rodou:

```bash
jupyter lab
```

dentro da pasta:

```
DATA SCIENCE & STATISTICAL COMPUTING
```

o Jupyter abriu **essa pasta como raiz do projeto**, por isso você vê:

```
aula_02_12_2026
aula_02_19_2026
aula_02_26_2026
...
```

Isso é o comportamento padrão.

---

# ✅ Sobre seu workflow (está quase perfeito)

Seu fluxo seria:

### 🏠 Em casa

```
abrir projeto
conda activate fiap-ds
jupyter lab
fazer alterações
git add .
git commit
git push
```

---

### 🏫 Na faculdade

```
git clone repositorio
cd DATA SCIENCE & STATISTICAL COMPUTING
conda env create -f environment_fiap-ds.yml
conda activate fiap-ds
jupyter lab
```

Depois:

```
git add .
git commit
git push
```

---

# ⚠️ Pequeno detalhe importante

O **ambiente conda não vai junto no Git**.

O que vai no Git é apenas:

```
environment_fiap-ds.yml
```

Então no PC da faculdade você precisa **criar o ambiente novamente**:

```bash
conda env create -f environment_fiap-ds.yml
```

Isso recria o mesmo ambiente.

---

# 💡 Fluxo real que Data Scientists usam

Projeto no Git:

```
project
 ├ notebooks
 ├ data
 ├ environment.yml
 └ README.md
```

Outro computador:

```
git clone projeto
conda env create -f environment.yml
conda activate env
jupyter lab
```

Ambiente **100% reproduzível**.

Você já está usando exatamente essa ideia.

---

# 🚀 Dica MUITO útil para seu caso (faculdade)

Para evitar esquecer de ativar ambiente, você pode abrir direto assim:

```bash
conda run -n fiap-ds jupyter lab
```

Assim o ambiente ativa automaticamente.

---

# 🔎 Um detalhe que pouca gente percebe

Se você estiver na faculdade e rodar:

```
jupyter lab
```

**sem ativar o ambiente**, o notebook pode usar o Python errado.

Então o ideal é sempre:

```
conda activate fiap-ds
jupyter lab
```

---

💡 Se quiser, posso te mostrar **uma melhoria pequena na sua estrutura que vai salvar muito tempo durante o semestre** (principalmente quando tiver **muitos notebooks e datasets** na disciplina).

# Abrindo jupyterlab com navegadores específicos

Sim — **o que aconteceu é exatamente o comportamento correto** 👍

Quando você rodou:

```bash
jupyter lab
```

dentro da pasta:

```
DATA SCIENCE & STATISTICAL COMPUTING
```

o Jupyter abriu **essa pasta como raiz do projeto**, por isso você vê:

```
aula_02_12_2026
aula_02_19_2026
aula_02_26_2026
...
```

Isso é o comportamento padrão.

---

# ✅ Sobre seu workflow (está quase perfeito)

Seu fluxo seria:

### 🏠 Em casa

```
abrir projeto
conda activate fiap-ds
jupyter lab
fazer alterações
git add .
git commit
git push
```

---

### 🏫 Na faculdade

```
git clone repositorio
cd DATA SCIENCE & STATISTICAL COMPUTING
conda env create -f environment_fiap-ds.yml
conda activate fiap-ds
jupyter lab
```

Depois:

```
git add .
git commit
git push
```

---

# ⚠️ Pequeno detalhe importante

O **ambiente conda não vai junto no Git**.

O que vai no Git é apenas:

```
environment_fiap-ds.yml
```

Então no PC da faculdade você precisa **criar o ambiente novamente**:

```bash
conda env create -f environment_fiap-ds.yml
```

Isso recria o mesmo ambiente.

---

# 💡 Fluxo real que Data Scientists usam

Projeto no Git:

```
project
 ├ notebooks
 ├ data
 ├ environment.yml
 └ README.md
```

Outro computador:

```
git clone projeto
conda env create -f environment.yml
conda activate env
jupyter lab
```

Ambiente **100% reproduzível**.

Você já está usando exatamente essa ideia.

---

# 🚀 Dica MUITO útil para seu caso (faculdade)

Para evitar esquecer de ativar ambiente, você pode abrir direto assim:

```bash
conda run -n fiap-ds jupyter lab
```

Assim o ambiente ativa automaticamente.

---

# 🔎 Um detalhe que pouca gente percebe

Se você estiver na faculdade e rodar:

```
jupyter lab
```

**sem ativar o ambiente**, o notebook pode usar o Python errado.

Então o ideal é sempre:

```
conda activate fiap-ds
jupyter lab
```

---

💡 Se quiser, posso te mostrar **uma melhoria pequena na sua estrutura que vai salvar muito tempo durante o semestre** (principalmente quando tiver **muitos notebooks e datasets** na disciplina).
