import DependenciasIntervalos as Dependencias

#Intervalo

#Clase
#Intervalos
# Un intervalo, un conjunto de pares ordenados
# Una serie de restriciones

#Indicar el maximo y el minimo de la tarea para poder hacer la misma operacion con otros intervalos.
#Tambien tenemos que controlar las constraint con los inversos.

class Intervalo:
    def __init__(x_inicio, x_fin ,y_inicio, y_fin , dependences):
        self.point_x_start = x_inicio
        self.point_y_start = y_inicio

        self.point_x_end = x_fin
        self.point_y_end = y_fin

        # Que punto de inicio esta antes.
        if self.point_x_start < self.point_y_start:
            self.point_start_main = self.point_x_start
        else:
            self.point_start_main = self.point_y_start

        #Que punto final esta despues de
        if self.point_x_end > self.point_y_end:
            self.point_end_main = self.point_x_end
        else:
            self.point_end_main = self.point_y_end


        self.misDependencias = []



        for dep in dependences:
            if isinstance(dep, int) is true
                if dep >0 && dep <14
                    if dep not in misDependencias:
                        misDependencias.append(dep)

      
print(Dependencias.DepenEnum.DURANTE.value)
print("BadSmell")