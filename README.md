[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/OcE5Fe4c)

# 1. Exploring Hyperparameters
Ich habe die Aufgabe innerhalb des Notebooks "hyperparameters.ipynb" geschrieben. Für 4 verschiedene Kernel sizes wird jeweils ein neues Modell trainiert, die prediction accuracy und inference time for predictions gemessen und in den nächsten Zellen geplottet, die Plots habe ich auch nochmal im Ordner unter "kernel_size_vs_accuracy.png" und "kernel_size_vs_inference_time.png" gespeichert und im Notebook diskutiert.

# 2. Gathering a Dataset
Ich habe mit dem notebook aus Aufgabe 1 "hyperparameters.ipynb" ein model auf like, peace und rock trainiert und es gespeichert und in den 02-dataset Ordner kopiert. Dieses Model wird geladen und mit diesem predicctions auf den neuen Bildern gemacht.

Die Bilder habe ich wie in dem HaGRID Subset im Ordner angeordnet und auch die Annotations zusammen geschrieben zur selben condition sodass ich den code aus dem alten notebook zum laden der neuen Bilder und annotations übernehmen konnte und aus diesen dann das neue testset erstellt habe.

# 3. Gesture-based Media Controls
Das Programm starten und Handgeste im grünen Rechteck ausführen, dieser frame wird für das model wie im training resized und darauf eine Geste predicted. 
Je nach Geste wird ein Media Player Befehl/Tastendruck ausgeführt. Es wird nur alle 1,5 Sekunden und mit einer ziemlich sicheren Prediction ein Befehl ausgeführt um spamming zu vermeiden, no gesture gibt es auch.

Das Modell habe ich mit dem notebook aus der Vorlesung trainiert und im Ordner gespeichert, es wird im Programm geladen. Ich habe auch vgg ausprobiert und fand es besser.

Steuerung: 
- like (Daumen Hoch) = Volume up
- dislike (Daumen runter) = Volume Down
- stop (Handfläche zeigen) = Start/stop
- two_up (Zwei finger zusammen hoch) = next

Falls die Erkennung nicht gut funktioniert, dann am besten einen weißen Hintergrund nehmen oder die Geste länger ausführen und die Hand anders positionieren.