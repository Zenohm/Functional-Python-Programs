def look_and_speak(end=30,inp=1):
    track = [0]
    main_list = [2,1]
    def delta_list(list):
        return [list[item+1]-list[item] for item in range(len(list)-1)]
    def get_chunk_indices(list):
        for x in range(len(delta_list(main_list))):
            if delta_list(main_list)[x]:
                track.append(x+1)
        return track.append(len(main_list))
    