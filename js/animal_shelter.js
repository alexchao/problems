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

    const AnimalQueue = function() {
        let first = undefined;
        let last = undefined;

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
            return toReturn;
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
            return animals[TYPE_DOG].remove();
        };

        const dequeueCat = function() {
            return animals[TYPE_CAT].remove();
        };

        return {
            enqueue: enqueue,
            dequeueAny: dequeueAny,
            dequeueDog: dequeueDog,
            dequeueCat: dequeueCat
        };
    };

    return {
        Animal: Animal,
        AnimalShelter: Shelter
    };
})();
