import Link from 'next/link';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-zinc-950 text-white">
      <div className="z-10 w-full max-w-5xl items-center justify-center font-mono text-sm flex flex-col space-y-8">
        <h1 className="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
          No-Code Builder
        </h1>
        <p className="text-xl text-zinc-400">Enterprise-grade website generation platform.</p>
        <Link 
          href="/builder" 
          className="px-8 py-4 bg-white text-black rounded-full font-bold hover:bg-zinc-200 transition-colors"
        >
          Enter Workspace
        </Link>
      </div>
    </main>
  );
}
