import { Testimonial } from "@/types/testimonials";

export function getTestimonials(): Testimonial[] {
  return [
    {
      id: 1,
      name: "John Doe",
      text: "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
    },
    {
      id: 2,
      name: "Jane Smith",
      text: "Sed ut perspiciatis unde omnis iste natus error sit voluptatem.",
    },
    {
      id: 3,
      name: "Alex Brown",
      text: "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.",
    },
    {
      id: 4,
      name: "Bob Johnson",
      text: "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium.",
    },
  ];
}
