function calcula ({ a, b }: { a: number; b: number; })
{
    return a + b;
}

let message: string = 'hola mundo';
console.log (message);
console.log(calcula({ a: 3, b: 5 }));
