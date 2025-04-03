Excellent question. Yes — there are many real situations where we can say a function is **O(f(n))**, but **not** \( \Theta(f(n)) \), because we don’t have a matching lower bound. Let's see a **concrete and simple example**:

---

## 🧠 Theoretical example:

Let’s define:

\[
T(n) = 
\begin{cases}
n & \text{if } n \text{ is even} \\
n^2 & \text{if } n \text{ is odd}
\end{cases}
\]

---

## ✅ Big-O Analysis

We ask: is there a function **f(n)** such that \( T(n) \leq c \cdot f(n) \) for all large enough \( n \)?

Pick \( f(n) = n^2 \)

We see:
- If \( n \) is odd: \( T(n) = n^2 = f(n) \)
- If \( n \) is even: \( T(n) = n < n^2 \)

So:

\[
T(n) \leq n^2 \quad \forall n
\Rightarrow T(n) = O(n^2)
\]

✅ We **can** say this is in **O(n²)**.

---

## ❌ But NOT Θ(n²)

To be in Θ(n²), we’d need both:
- \( T(n) = O(n^2) \)
- \( T(n) = \Omega(n^2) \)

But:

- For all **even** \( n \), \( T(n) = n \)
- So:
  \[
  \frac{T(n)}{n^2} = \frac{n}{n^2} = \frac{1}{n} \rightarrow 0
  \]

Hence:

\[
T(n) \notin \Omega(n^2)
\Rightarrow T(n) \notin \Theta(n^2)
\]

---

## ✅ Real-world example

Suppose you're analyzing an algorithm that:
- On **sorted input** runs in **O(n)**
- On **worst-case input**, runs in **O(n log n)**

If you don't know the distribution of inputs (or you're measuring **worst-case only**), you might say:

\[
T(n) = O(n \log n)
\]

But you **cannot** say \( \Theta(n \log n) \) unless that’s the behavior **on all large inputs**, not just worst-case.

---

## 🧠 Summary

| Can we say...             | When                          |
|---------------------------|-------------------------------|
| \( T(n) = O(f(n)) \)      | If it **never grows faster** than \( f(n) \) |
| \( T(n) = \Theta(f(n)) \) | If it **always grows like** \( f(n) \) — both upper and lower bounds match |
| Only \( O(f(n)) \)        | When the function **sometimes grows slower** |

---

Let me know if you want an example from actual algorithms (like quicksort or hashing collisions) where we use just \( O \), not \( \Theta \).
