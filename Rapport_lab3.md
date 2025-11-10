# optimisation_notes.md

## Lab 3 — Optimisation et fiabilité du cluster Spark

### 1. Objectif
Optimiser les performances du pipeline Spark en testant différents niveaux de partitionnement, en utilisant le cache, le broadcast join et les checkpoints pour la tolérance aux pannes.

---

### 2. Partitionnement

Nous avons testé trois niveaux de partitionnement pour le DataFrame `df_logs` :

| Nb de partitions | Temps d'exécution (s) |
|-----------------|---------------------|
| 2               | 1.30                |
| 4               | 0.55                |
| 8               | 0.59                |

Observations :  
- Avec 2 partitions, le temps est plus long car le parallélisme est limité.  
- Avec 4 partitions, on atteint le temps minimum.  
- Avec 8 partitions, le temps augmente légèrement à cause de l’overhead de gestion des tâches.  

Conclusion : un nombre de partitions adapté au cluster permet de maximiser les performances, ni trop peu, ni trop élevé.

---

### 3. Broadcast Join

Pour la jointure avec `df_users`, nous avons utilisé un broadcast join :

```python
df_joined = df_visits.join(broadcast(df_users), "user_id")
