def is_piece_in_collection(collection, current_piece):
    if current_piece in collection:
        return True
    return False


def add_command(collection, piece_info):
    current_piece, composer, current_key = piece_info
    if is_piece_in_collection(collection, current_piece):
        print(f"{current_piece} is already in the collection!")
    else:
        collection[current_piece] = {'composer': composer, 'key': current_key}
        print(f"{current_piece} by {composer} in {current_key} added to the collection!")
    return collection


def remove_command(collection, piece_info):
    current_piece = piece_info[0]
    if is_piece_in_collection(collection, current_piece):
        collection.pop(current_piece)
        print(f"Successfully removed {current_piece}!")
    else:
        print(f"Invalid operation! {current_piece} does not exist in the collection.")
    return collection


def change_key_command(collection, piece_info):
    current_piece, current_key = piece_info
    if is_piece_in_collection(collection, current_piece):
        collection[current_piece]['key'] = current_key
        print(f"Changed the key of {current_piece} to {current_key}!")
    else:
        print(f"Invalid operation! {current_piece} does not exist in the collection.")
    return collection


number_of_pieces = int(input())

collection_of_pieces = {}

for _ in range(number_of_pieces):
    piece, composer_name, key_type = input().split("|")
    collection_of_pieces[piece] = {'composer': composer_name, 'key': key_type}

data = input()

while not data == "Stop":
    data_info = data.split("|")
    command = data_info[0]
    if command == "Add":
        piece_data = data_info[1:]
        add_command(collection_of_pieces, piece_data)
    elif command == "Remove":
        piece_data = data_info[1:]
        remove_command(collection_of_pieces, piece_data)
    elif command == "ChangeKey":
        piece_data = data_info[1:]
        change_key_command(collection_of_pieces, piece_data)
    data = input()


sorted_collection = sorted(collection_of_pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for i in sorted_collection:
    print(f"{i[0]} -> Composer: {i[1]['composer']}, Key: {i[1]['key']}")
