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
