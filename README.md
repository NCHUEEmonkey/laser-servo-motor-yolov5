# laser-servo-motor-yolov5
先做出機械結構，再上傳code到arduino
去下載yolov5資料夾，就可以辨識
#(COCO 0: 'person')
        for *xyxy, conf, cls in results.xyxy[0]:
            if int(cls) == 0:  # 只保留 'person'
                x1, y1, x2, y2 = map(int, xyxy)
                w, h = x2 - x1, y2 - y1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                send_coordinates_to_arduino(x1, y1, w, h)
0 - Person
1 - Bicycle
2 - Car
3 - Motorcycle
4 - Airplane
5 - Bus
6 - Train
7 - Truck
8 - Boat
9 - Traffic Light
10 - Fire Hydrant
11 - Stop Sign
12 - Parking Meter
13 - Bench
14 - Bird
15 - Cat
16 - Dog
17 - Horse
18 - Sheep
19 - Cow
20 - Elephant
21 - Bear
22 - Zebra
23 - Giraffe
24 - Backpack
25 - Umbrella
26 - Handbag
27 - Tie
28 - Suitcase
29 - Frisbee
30 - Skis
31 - Snowboard
32 - Sports Ball
33 - Kite
34 - Baseball Bat
35 - Baseball Glove
36 - Skateboard
37 - Surfboard
38 - Tennis Racket
39 - Bottle
40 - Wine Glass
41 - Cup
42 - Fork
43 - Knife
44 - Spoon
45 - Bowl
46 - Banana
47 - Apple
48 - Sandwich
49 - Orange
50 - Broccoli
51 - Carrot
52 - Hot Dog
53 - Pizza
54 - Donut
55 - Cake
56 - Chair
57 - Couch
58 - Potted Plant
59 - Bed
60 - Dining Table
61 - Toilet
62 - TV
63 - Laptop
64 - Mouse
65 - Remote
66 - Keyboard
67 - Cell Phone
68 - Microwave
69 - Oven
70 - Toaster
71 - Sink
72 - Refrigerator
73 - Book
74 - Clock
75 - Vase
76 - Scissors
77 - Teddy Bear
78 - Hair Drier
79 - Toothbrush
