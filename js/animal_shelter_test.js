const AS = require('./animal_shelter.js').AS;
const Test = require('./test.js');
const A = Test.Assert;


const animalQueueTests = {
    'emptyQueue': function() {
        const q = AS.AnimalQueue();
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
    }
};


Test.runTests(animalQueueTests);
