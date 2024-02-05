import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


class IR:
    _tranches = [28000, 40000, 50000, 60000, 150000]
    _tauxIR = [0, 12, 24, 34, 38, 40]

    @staticmethod
    def getIR(salaire):
        for i in range(len(IR._tranches)):
            if salaire <= IR._tranches[i]:
                return IR._tauxIR[i] / 100

class IEmploye:
    def Age(self):
        pass

    def Anciennete(self):
        pass

    def DateRetraite(self, ageRetraite):
        pass

class Employe(IEmploye):
    _mtle_auto_increment = 0

    def __init__(self, nom, date_naissance, date_embauche, salaire_base):
        self._mtle = Employe._mtle_auto_increment
        Employe._mtle_auto_increment += 1
        self._nom = nom
        self._dateNaissance = datetime.strptime(date_naissance, "%Y-%m-%d")
        self._dateEmbauche = datetime.strptime(date_embauche, "%Y-%m-%d")
        self._salaireBase = salaire_base

        if self.Age() < 16:
            raise ValueError("L'employé ne peut pas être recruté avant l'âge de 16 ans.")

    def DateEmbauche(self):
        return self._dateEmbauche

    def DateNaissance(self):
        return self._dateNaissance

    def Age(self):
        today = datetime.now()
        return today.year - self._dateNaissance.year - ((today.month, today.day) < (self._dateNaissance.month, self._dateNaissance.day))

    def Anciennete(self):
        today = datetime.now()
        return today.year - self._dateEmbauche.year - ((today.month, today.day) < (self._dateEmbauche.month, self._dateEmbauche.day))

    def DateRetraite(self, ageRetraite):
        return self._dateNaissance.year + ageRetraite

    def SalaireAPayer(self):
        pass

    def __eq__(self, other):
        return self._mtle == other._mtle

    def __lt__(self, other):
        return self._nom < other._nom

    def __str__(self):
        return f"{self._mtle}-{self._nom}-{self._dateNaissance.strftime('%Y-%m-%d')}-{self._dateEmbauche.strftime('%Y-%m-%d')}-{self._salaireBase}"

class Formateur(Employe):
    def __init__(self, nom, date_naissance, date_embauche, salaire_base, heure_sup=0, remuneration_hsup=70.00):
        super().__init__(nom, date_naissance, date_embauche, salaire_base)
        self._heureSup = heure_sup
        self._remunerationHSup = remuneration_hsup

    def SalaireAPayer(self):
        taux_ir = IR.getIR(self._salaireBase + self._heureSup * self._remunerationHSup)
        salaire_net = (self._salaireBase + self._heureSup * self._remunerationHSup) * (1 - taux_ir)
        return salaire_net

    def __str__(self):
        return f"{super().__str__}-{self._heureSup}-{self._remunerationHSup}"

class Agent(Employe):
    def __init__(self, nom, date_naissance, date_embauche, salaire_base, prime_responsabilite):
        super().__init__(nom, date_naissance, date_embauche, salaire_base)
        self._primeResponsabilite = prime_responsabilite

    def SalaireAPayer(self):
        taux_ir = IR.getIR(self._salaireBase + self._primeResponsabilite)
        salaire_net = (self._salaireBase + self._primeResponsabilite) * (1 - taux_ir)
        return salaire_net

    def __str__(self):
        return f"{super().__str__}-{self._primeResponsabilite}"

class SalaryCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salary Calculator")

        self.create_widgets()

    def create_widgets(self):

        formateur_frame = ttk.LabelFrame(self.root, text="Formateur")
        formateur_frame.grid(row=0, column=0, padx=10, pady=10)



        ttk.Button(formateur_frame, text="Ajouter Formateur", command=self.add_formateur).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(formateur_frame, text="Calculer Salaire", command=self.calculate_formateur_salary).grid(row=7, column=0, columnspan=2, pady=10)

        agent_frame = ttk.LabelFrame(self.root, text="Agent")
        agent_frame.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(agent_frame, text="Ajouter Agent", command=self.add_agent).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(agent_frame, text="Calculer Salaire", command=self.calculate_agent_salary).grid(row=6, column=0, columnspan=2, pady=10)

    def add_formateur(self):
        nom = self.formateur_nom_entry.get()
        date_naissance = self.formateur_dob_entry.get()
        date_embauche = self.formateur_doe_entry.get()
        salaire_base = float(self.formateur_salaire_entry.get())
        heure_sup = int(self.formateur_heure_sup_entry.get())
        remuneration_hsup = float(self.formateur_taux_hsup_entry.get())

        formateur = Formateur(nom, date_naissance, date_embauche, salaire_base, heure_sup, remuneration_hsup)
        result_text = f"Formateur {nom} ajouté avec succès!"
        messagebox.showinfo("Résultat", result_text)

    def calculate_formateur_salary(self):


    def add_agent(self):
        nom = self.agent_nom_entry.get()
        date_naissance = self.agent_dob_entry.get()
        date_embauche = self.agent_doe_entry.get()
        salaire_base = float(self.agent_salaire_entry.get())
        prime_responsabilite = float(self.agent_prime_responsabilite_entry.get())

        agent = Agent(nom, date_naissance, date_embauche, salaire_base, prime_responsabilite)
        result_text = f"Agent {nom} ajouté avec succès!"
        messagebox.showinfo("Résultat", result_text)

    def calculate_agent_salary(self):
  

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryCalculatorApp(root)
    root.mainloop()
