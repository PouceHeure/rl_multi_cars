


if __name__ == "__main__":
    pygame.init()
    c = City(points_initial=[[200,100],[75,35],[25,100]])
    c.build()
    c.show()
    while True:
        pygame.display.flip()
