# Projet Graphes et langages
Gestion d’un réseau de bus
Structure de données
Proposez une ou plusieurs structures de données permettant de modélisez un réseau de bus, en tenant
compte de dimanches jours fériés, nuit et vacances.
Vous implémenterez un exemple en vous appuyant sur une partie du réseau de la SIBRA.
• Implémentez la structure de données
• Implémentez des méthodes facilitant la saisie de données
• Implémentez l'exemple
Algorithmique
Implémentez un algorithme qui calcul le plus court chemin entre 2 arrêts de bus avec plusieurs options,
dans tous les cas il faudra préciser une date de départ (au minimum un horaire) prendre en compte les
départs immédiatement postérieurs à la date (horaire) donnée et prendre en compte les temps d’attente
en cas de changement de ligne :
• Shortest: le plus court, en nombre d'arc
• Fastest: le plus rapide, mais avec potentiellement plus d'arc
• Foremost: arrive au plus tôt, peut importe le nombres d'arc
