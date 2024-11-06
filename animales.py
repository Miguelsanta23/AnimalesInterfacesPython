# Definición de las interfaces
class VolarAble:
    def volar(self):
        pass


class NadarAble:
    def nadar(self):
        pass


class TerrestreAble:
    def desplazar(self):
        pass


class RespirarAble:
    def respirar(self):
        pass




# Implementación de las clases de animales
class Pato(VolarAble, NadarAble, TerrestreAble, RespirarAble):
    def respirar(self):
        print("El pato respira")

    def volar(self):
        print("El pato vuela")

    def nadar(self):
        print("El pato nada")

    def desplazar(self):
        print("El pato se desplaza")


class Elefante(TerrestreAble, RespirarAble, NadarAble):
    def respirar(self):
        print("El elefante respira")

    def nadar(self):
        print("El elefante nada")

    def desplazar(self):
        print("El elefante se desplaza")



class Cocodrilo(NadarAble, TerrestreAble, RespirarAble):
    def respirar(self):
        print("El cocodrilo respira")

    def nadar(self):
        print("El cocodrilo nada")

    def desplazar(self):
        print("El cocodrilo se desplaza")


class Leon(TerrestreAble, RespirarAble):
    def respirar(self):
        print("El leon respira")

    def desplazar(self):
        print("El leon se desplaza")


class Aguila(VolarAble, RespirarAble):
    def respirar(self):
        print("El aguila respira")

    def volar(self):
        print("El aguila vuela")

    def desplazar(self):
        print("El aguila se desplaza")


class Tiburon(NadarAble, RespirarAble):
    def respirar(self):
        print("El tiburon respira")

    def nadar(self):
        print("El tiburon nada")


# Realizacion de las acciones de los animales
def main():
    pato = Pato()
    elefante = Elefante()
    cocodrilo = Cocodrilo()
    leon = Leon()
    aguila = Aguila()
    tiburon = Tiburon()


    print("Pato:")
    pato.volar()
    pato.nadar()
    pato.desplazar()
    pato.respirar()

    print("Elefante:")
    elefante.desplazar()
    elefante.respirar()
    elefante.nadar()

    print("Cocodrilo:")
    cocodrilo.nadar()
    cocodrilo.desplazar()
    cocodrilo.respirar()

    print("Leon:")
    leon.desplazar()
    leon.respirar()

    print("Aguila:")
    aguila.volar()
    aguila.respirar()
    aguila.desplazar()

    print("Tiburon:")
    tiburon.nadar()
    tiburon.respirar()

if __name__ == "__main__":
    main()