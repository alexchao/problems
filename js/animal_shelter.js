const AS = (function() {

    const TYPE_DOG = 'dog';
    const TYPE_CAT = 'cat';

    const LinkedList = function(data) {
        return { next: null, data: data };
    };

    /* An animal that has been enqueued. Has an orderId */
    const QAnimal = function(orderId, animal) {
        return { orderId: orderId, animal: animal };
    };

    const Animal = function(type, name) {
        return { type: type, name: name };
    };

    const Dog = function(name) {
        return Animal(TYPE_DOG, name);
    };

    const Cat = function(name) {
        return Animal(TYPE_CAT, name);
    };

    const AnimalQueue = function() {
        let first = null;
        let last = null;

        const add = function(qAnimal) {
            const newNode = LinkedList(qAnimal);
            if (!first) {
                first = newNode;
            } else {
                last.next = newNode;
            }
            last = newNode;
        };

        const remove = function() {
            if (!first) {
                return null;
            }

            const toReturn = first;
            first = first.next;

            if (!first) {
                last = null;
            }

            return toReturn.data;
        };

        const peekOrderId = function() {
            if (!last) {
                return null;
            }

            return first.data.orderId;
        };

        return {
            add: add,
            remove: remove,
            peekOrderId: peekOrderId
        };
    };

    const Shelter = function() {

        let orderId = 0;
        const animals = {
            [TYPE_DOG]: AnimalQueue(),
            [TYPE_CAT]: AnimalQueue()
        };

        const enqueue = function(animal) {
            const qAnimal = QAnimal(orderId, animal);
            animals[animal.type].add(qAnimal);
            orderId++;
        };

        const dequeueAny = function() {
            const dogOrderId = animals[TYPE_DOG].peekOrderId();
            const catOrderId = animals[TYPE_CAT].peekOrderId();

            if (dogOrderId !== null && catOrderId !== null) {
                if (dogOrderId < catOrderId) {
                    return dequeueDog();
                } else {
                    return dequeueCat();
                }
            }

            if (dogOrderId !== null) {
                return dequeueDog();
            }

            if (catOrderId !== null) {
                return dequeueCat();
            }

            return null;
        };

        const dequeueDog = function() {
            return _dequeue(TYPE_DOG);
        };

        const dequeueCat = function() {
            return _dequeue(TYPE_CAT);
        };

        const _dequeue = function(type) {
            const qAnimal = animals[type].remove();
            return qAnimal ? qAnimal.animal : null;
        };

        return {
            enqueue: enqueue,
            dequeueAny: dequeueAny,
            dequeueDog: dequeueDog,
            dequeueCat: dequeueCat
        };
    };

    return {
        Dog: Dog,
        Cat: Cat,
        Animal: Animal,
        QueuedAnimal: QAnimal,
        AnimalQueue: AnimalQueue,
        AnimalShelter: Shelter
    };
})();


exports.AS = AS;
