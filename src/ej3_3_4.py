def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)   
    frutas_comunes = set_frutas1|~~set_frutas2
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    print(f"Las frutas que estan en ambas listas son: {frutas_comunes}.\nEstas son las no comunes de fruta 1 {frutas_solo_en_frutas1}\nEstas son las no comunes de fruta 2 {frutas_solo_en_frutas2}. ")
        
if __name__ == "__main__":
    main()