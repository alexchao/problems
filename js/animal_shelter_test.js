const AS = require('./animal_shelter.js').AS;
const Test = require('./test.js');
const A = Test.Assert;


const animalQueueTests = {
    'emptyQueue': function() {
        const q = AS.AnimalQueue();
        A.assertNull(q.peekOrderId());
        A.assertNull(q.remove());
        A.assertNull(q.peekOrderId());
    },
    'addFirst': function() {
        const q = AS.AnimalQueue();
        const dog = AS.Dog('Max');
        const qAnimal = AS.QueuedAnimal(123, dog);
        q.add(qAnimal);
        A.assertEqual(q.peekOrderId(), 123);
        A.assertEqual(q.remove(), qAnimal);
        A.assertNull(q.remove());
        A.assertNull(q.peekOrderId());
    },
    'addManyRemoveMany': function() {
        const q = AS.AnimalQueue();

        // Add 5
        const qa1 = AS.QueuedAnimal(1, {});
        const qa2 = AS.QueuedAnimal(2, {});
        const qa3 = AS.QueuedAnimal(3, {});
        const qa4 = AS.QueuedAnimal(4, {});
        const qa5 = AS.QueuedAnimal(5, {});
        [qa1, qa2, qa3, qa4, qa5].forEach(function(qa) {
            q.add(qa);
            A.assertEqual(q.peekOrderId(), qa1.orderId);
        });

        // Remove 2
        A.assertEqual(q.remove(), qa1);
        A.assertEqual(q.peekOrderId(), qa2.orderId);
        A.assertEqual(q.remove(), qa2);
        A.assertEqual(q.peekOrderId(), qa3.orderId);

        // Add 1
        const qa6 = AS.QueuedAnimal(6, {});
        q.add(qa6);

        // Remove all remaining
        [qa3, qa4, qa5, qa6].forEach(function(qa) {
            A.assertEqual(q.peekOrderId(), qa.orderId);
            A.assertEqual(q.remove(), qa);
        });

        A.assertNull(q.peekOrderId());
        A.assertNull(q.remove());
    }
};

// TODO: kill all the duplication in here with some sort of
// setup/teardown functionality
const shelterTests = {
    'emptyShelter': function() {
        const s = AS.AnimalShelter();
        A.assertNull(s.dequeueAny());
        A.assertNull(s.dequeueDog());
        A.assertNull(s.dequeueCat());
    },
    'queueDogAndDequeueAny': function() {
        const s = AS.AnimalShelter();
        const dog = AS.Dog('Odie');
        s.enqueue(dog);
        A.assertEqual(s.dequeueAny(), dog);
        A.assertNull(s.dequeueAny());
    },
    'queueCatAndDequeueAny': function() {
        const s = AS.AnimalShelter();
        const cat = AS.Cat('Garfield');
        s.enqueue(cat);
        A.assertEqual(s.dequeueAny(), cat);
        A.assertNull(s.dequeueAny());
    },
    'queueDogAndDequeueDog': function() {
        const s = AS.AnimalShelter();
        const dog = AS.Dog('Odie');
        s.enqueue(dog);
        A.assertNull(s.dequeueCat());
        A.assertEqual(s.dequeueDog(), dog);
        A.assertNull(s.dequeueDog());
    },
    'queueCatAndDequeueCat': function() {
        const s = AS.AnimalShelter();
        const cat = AS.Cat('Garfield');
        s.enqueue(cat);
        A.assertNull(s.dequeueDog());
        A.assertEqual(s.dequeueCat(), cat);
        A.assertNull(s.dequeueCat());
    },
    'queueManyDequeueCats': function() {
        const s = AS.AnimalShelter();
        const d1 = AS.Dog('Max');
        const d2 = AS.Dog('Peppy');
        const d3 = AS.Dog('Odie');
        const c1 = AS.Cat('Garfield');
        const c2 = AS.Cat('Tigger');
        const c3 = AS.Cat('Heathcliff');

        [d1, c1, c2, d2, d3, c3].forEach(function(a) {
            s.enqueue(a);
        });
        [c1, c2, c3].forEach(function(a) {
            A.assertEqual(s.dequeueCat(), a);
        });
        A.assertNull(s.dequeueCat());
    },
    'queueManyDequeueDogs': function() {
        const s = AS.AnimalShelter();
        const d1 = AS.Dog('Max');
        const d2 = AS.Dog('Peppy');
        const d3 = AS.Dog('Odie');
        const c1 = AS.Cat('Garfield');
        const c2 = AS.Cat('Tigger');
        const c3 = AS.Cat('Heathcliff');

        [d1, c1, c2, d2, d3, c3].forEach(function(a) {
            s.enqueue(a);
        });
        [d1, d2, d3].forEach(function(a) {
            A.assertEqual(s.dequeueDog(), a);
        });
        A.assertNull(s.dequeueDog());
    },
    'queueManyDequeueMixed': function() {
        const s = AS.AnimalShelter();
        const d1 = AS.Dog('Max');
        const d2 = AS.Dog('Peppy');
        const d3 = AS.Dog('Odie');
        const d4 = AS.Dog('Lassie');
        const c1 = AS.Cat('Garfield');
        const c2 = AS.Cat('Tigger');
        const c3 = AS.Cat('Heathcliff');
        const c4 = AS.Cat('Nermal');

        [d1, c1, c2, d2, d3, c3].forEach(function(a) {
            s.enqueue(a);
        });
        A.assertEqual(s.dequeueCat(), c1);
        A.assertEqual(s.dequeueCat(), c2);
        A.assertEqual(s.dequeueAny(), d1);

        [c4, d4].forEach(function(a) { s.enqueue(a); });

        A.assertEqual(s.dequeueCat(), c3);
        A.assertEqual(s.dequeueAny(), d2);
        A.assertEqual(s.dequeueAny(), d3);
        A.assertEqual(s.dequeueDog(), d4);
        A.assertNull(s.dequeueDog());
        A.assertEqual(s.dequeueAny(), c4);
        A.assertNull(s.dequeueCat());
    }
};


Test.runTests(animalQueueTests);
Test.runTests(shelterTests);
