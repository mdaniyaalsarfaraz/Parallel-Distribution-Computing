import multiprocessing

def create_items(pipe):
    send_end, _ = pipe  # send_end will send data
    for item in range(10):
        send_end.send(item)
    send_end.close()  # signal EOF

def multiply_items(input_pipe, output_pipe):
    recv_end, _ = input_pipe  # receive from first pipe
    send_end, _ = output_pipe  # send to second pipe
    try:
        while True:
            item = recv_end.recv()
            send_end.send(item * item)
    except EOFError:
        send_end.close()  # close output pipe when done

if __name__ == '__main__':
    # First pipe
    pipe_1 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    p1.start()

    # Second pipe
    pipe_2 = multiprocessing.Pipe(True)
    p2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2))
    p2.start()

    # Close unused ends in main
    pipe_1[0].close()
    pipe_2[0].close()

    # Receive results
    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End")

    # Wait for processes to finish
    p1.join()
    p2.join()
