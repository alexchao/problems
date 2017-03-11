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

        // Remove all
        [qa3, qa4, qa5, qa6].forEach(function(qa) {
            A.assertEqual(q.peekOrderId(), qa.orderId);
            A.assertEqual(q.remove(), qa);
        });

        A.assertNull(q.peekOrderId());
        A.assertNull(q.remove());
    }
};


Test.runTests(animalQueueTests);
